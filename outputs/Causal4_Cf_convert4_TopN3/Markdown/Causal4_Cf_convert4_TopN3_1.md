
# Parameters

    Name :                      Causal4_Cf_convert4_TopN3-1
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67057311517 function calls (66770973694 primitive calls) in 86115.94 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.943 86115.943 {built-in method builtins.exec}
                      1    5.075    5.075 86115.943 86115.943 <string>:1(<module>)
                      1  433.470  433.470 86110.868 86110.868 main.py:79(CFagent)
                9262545   45.608    0.000 24729.696    0.003 agent.py:29(learn)
                3087515   19.360    0.000 21129.144    0.007 game.py:41(step)
                3087515   21.299    0.000 20312.197    0.007 layers.py:718(step)
                9262540  644.198    0.000 19855.822    0.002 learner.py:42(Qlearn)
                3087515  306.872    0.000 13014.007    0.004 layers.py:17(step)
              308315415  965.427    0.000 12679.619    0.000 layer.py:98(move)
        320489188/34153056 1427.758    0.000 11345.961    0.000 module.py:866(_call_impl)
               24890516   76.567    0.000 10534.169    0.000 network.py:27(forward)
               24890516  361.802    0.000 10270.307    0.000 container.py:117(forward)
                3087515  890.755    0.000 10253.707    0.003 agent.py:210(counterfact)
                3087515  402.970    0.000 9634.767    0.003 agent.py:54(_learn)
                3087515  395.994    0.000 8700.014    0.003 agent.py:202(_learn)
                3087515 7139.499    0.002 8238.910    0.003 replaybuffer.py:22(sample_data)
                3087515 6889.406    0.002 7922.394    0.003 replaybuffer.py:67(sample_data)
              308315415 1428.896    0.000 7800.537    0.000 layers.py:735(check)
                9262540  101.460    0.000 7556.310    0.001 optimizer.py:84(wrapper)
                3087516  475.199    0.000 7240.593    0.002 layers.py:684(update)
                9262540   54.407    0.000 7129.670    0.001 grad_mode.py:24(decorate_context)
                9262540  332.103    0.000 6954.122    0.001 adam.py:55(step)
                3087515  112.976    0.000 6323.354    0.002 agent.py:117(_learn)
                9262540 1439.938    0.000 6286.459    0.001 _functional.py:53(adam)
                7810746  273.250    0.000 5630.633    0.001 agent.py:49(__call__)
                9262540   45.061    0.000 5306.215    0.001 tensor.py:195(backward)
               48892986 5301.945    0.000 5301.945    0.000 {built-in method tensor}
                9262540   54.078    0.000 5259.808    0.001 __init__.py:68(backward)
               41764373   29.059    0.000 5108.824    0.000 game.py:37(board)
               61750310 2917.636    0.000 4997.232    0.000 layer.py:151(update)
                9262540 4984.333    0.001 4984.333    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3087515 1729.839    0.001 3888.001    0.001 agent.py:88(interveen)
               49781032  119.726    0.000 3857.372    0.000 conv.py:398(forward)
               49781032   95.039    0.000 3676.978    0.000 conv.py:390(_conv_forward)
               49781032 3581.939    0.000 3581.939    0.000 {built-in method conv2d}
                3087515 1949.450    0.001 3359.461    0.001 replaybuffer.py:28(teleporter_save_data)
              308315415  530.730    0.000 3261.344    0.000 layers.py:729(isFree)
               68496518  143.959    0.000 2887.075    0.000 linear.py:93(forward)
             2548247803 2319.931    0.000 2730.614    0.000 layer.py:95(isFree)
               68496518   62.581    0.000 2661.967    0.000 functional.py:1737(linear)
               68496518 2584.919    0.000 2584.919    0.000 {built-in method torch._C._nn.linear}
                3087515 1649.907    0.001 2541.892    0.001 agent.py:67(modify)
                1642205   40.414    0.000 2431.179    0.001 agent.py:175(choose_action)
               41773386 1727.427    0.000 1727.427    0.000 {built-in method cat}
               10898261   90.365    0.000 1614.821    0.000 agent.py:59(modify_board)
             5809567963 1088.602    0.000 1542.547    0.000 enum.py:646(__hash__)
                3087510   70.696    0.000 1536.978    0.000 agent.py:171(__call__)
               93387034   87.076    0.000 1487.990    0.000 activation.py:713(forward)
              308767128  323.134    0.000 1426.522    0.000 {built-in method builtins.any}
               93387034   87.484    0.000 1400.914    0.000 functional.py:1364(leaky_relu)
              133880165 1399.682    0.000 1399.682    0.000 {built-in method clone}
                3087515   69.700    0.000 1392.012    0.000 agent.py:112(__call__)
              308751600  243.823    0.000 1354.590    0.000 {built-in method builtins.all}
               93387034 1298.057    0.000 1298.057    0.000 {built-in method torch._C._nn.leaky_relu}
             1036568104 1294.149    0.000 1294.149    0.000 layer.py:146(elements)
              308315415  968.337    0.000 1256.711    0.000 layers.py:77(check)
              172900740 1232.709    0.000 1232.709    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3071988   44.432    0.000 1211.761    0.000 layers.py:740(restart)
                3087515  931.069    0.000 1173.362    0.000 replaybuffer.py:73(CF_save_data)
              308315415  759.435    0.000 1160.170    0.000 layers.py:286(check)
             2840588482  748.749    0.000 1147.842    0.000 layers.py:690(<genexpr>)
             3362475732  913.719    0.000 1103.387    0.000 layers.py:700(<genexpr>)
              172900740 1082.079    0.000 1082.079    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9262540  198.380    0.000 1073.860    0.000 optimizer.py:189(zero_grad)
               10898261 1062.708    0.000 1062.708    0.000 {built-in method torch._C._nn.one_hot}
              308315415  652.777    0.000 1038.259    0.000 layers.py:246(check)
                3071988   20.392    0.000  854.156    0.000 level.py:8(__init__)
                3087515   73.584    0.000  827.259    0.000 replaybuffer.py:18(stacker)
                3087510   73.228    0.000  775.935    0.000 replaybuffer.py:63(stacker)
              308315415  573.319    0.000  722.069    0.000 layers.py:62(check)
               86450370  713.165    0.000  713.165    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7506660731  691.172    0.000  691.172    0.000 layer.py:91(positions)
                3071988  111.873    0.000  668.860    0.000 levels.py:199(generate)
               86450370  627.689    0.000  627.689    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        8143439594/8143439591  541.536    0.000  611.219    0.000 {built-in method builtins.len}
                7810746  210.979    0.000  590.136    0.000 exploration.py:53(softmaxer)
              308315415  388.702    0.000  587.747    0.000 layers.py:313(check)
               86450370  587.234    0.000  587.234    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               86450370  577.442    0.000  577.442    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               12319006  225.150    0.000  573.553    0.000 random.py:315(sample)
              308315415  329.286    0.000  519.704    0.000 layers.py:273(check)
              605152674  411.322    0.000  507.310    0.000 tensor.py:906(grad)
                9262540   20.174    0.000  490.075    0.000 loss.py:527(forward)
                1642205  411.308    0.000  484.723    0.000 agent.py:186(convert_values)
                3087515  282.148    0.000  483.540    0.000 collector.py:46(collect)
                9262540   55.010    0.000  469.901    0.000 functional.py:2898(mse_loss)
             5809603162  453.951    0.000  453.951    0.000 {built-in method builtins.hash}
                6143976   53.480    0.000  447.268    0.000 level.py:41(notUsed)
              308315415  306.346    0.000  443.639    0.000 layers.py:48(check)
               86450370  420.896    0.000  420.896    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              308315415  230.442    0.000  336.961    0.000 layers.py:23(check)
              147865936  313.578    0.000  313.578    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              276373376  215.856    0.000  306.097    0.000 layer.py:126(remove)
               30719880   45.461    0.000  302.549    0.000 layer.py:69(restart)
              457327410  205.711    0.000  287.879    0.000 layer.py:130(add)
               61750310  284.609    0.000  284.609    0.000 layer.py:163(<listcomp>)
             3404209129  280.381    0.000  280.381    0.000 {method 'random' of '_random.Random' objects}
                9262540  276.342    0.000  276.342    0.000 {built-in method torch._C._nn.mse_loss}
                6175032  275.045    0.000  275.045    0.000 {built-in method nonzero}
              375045057  176.687    0.000  265.275    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551819: <Causal4_Cf_convert4_TopN3_1> in cluster <dcc> Done

Job <Causal4_Cf_convert4_TopN3_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:32 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 23 06:18:35 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 06:18:35 2021
Terminated at Sat Apr 24 06:13:59 2021
Results reported at Sat Apr 24 06:13:59 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85907.77 sec.
    Max Memory :                                 9309 MB
    Average Memory :                             6430.43 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7075.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86126 sec.
    Turnaround time :                            269607 sec.

The output (if any) is above this job summary.

