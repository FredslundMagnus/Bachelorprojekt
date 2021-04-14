
# Parameters

    Name :                      ReTest1-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        500000.0
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      34334212034 function calls (34180207719 primitive calls) in 42912.70 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42912.703 42912.703 {built-in method builtins.exec}
                      1    3.911    3.911 42912.703 42912.703 <string>:1(<module>)
                      1  228.494  228.494 42908.791 42908.791 main.py:75(CFagent)
                5765958   24.119    0.000 14488.138    0.003 agent.py:29(learn)
                5760695  364.614    0.000 11681.488    0.002 learner.py:42(Qlearn)
                1921986    9.796    0.000 10089.002    0.005 game.py:41(step)
                1921986   14.757    0.000 9658.287    0.005 layers.py:718(step)
                1921986  189.106    0.000 6017.407    0.003 layers.py:17(step)
        173237533/19234909  749.071    0.000 5856.809    0.000 module.py:866(_call_impl)
              191913582  324.739    0.000 5810.947    0.000 layer.py:98(move)
                1921986  238.965    0.000 5655.492    0.003 agent.py:54(_learn)
               13474214   38.864    0.000 5413.158    0.000 network.py:24(forward)
               13474214  187.872    0.000 5277.014    0.000 container.py:117(forward)
                1921986  230.755    0.000 5129.435    0.003 agent.py:202(_learn)
                5760695   53.881    0.000 4461.211    0.001 optimizer.py:84(wrapper)
                5760695   28.580    0.000 4221.579    0.001 grad_mode.py:24(decorate_context)
                5760695  189.433    0.000 4128.777    0.001 adam.py:55(step)
                5760695  855.190    0.000 3732.391    0.001 _functional.py:53(adam)
                1921986   61.102    0.000 3665.309    0.002 agent.py:117(_learn)
                1921987  298.965    0.000 3605.524    0.002 layers.py:684(update)
                1921986 2971.999    0.002 3596.191    0.002 replaybuffer.py:22(sample_data)
                1921986  377.647    0.000 3301.825    0.002 agent.py:210(counterfact)
              191913582  681.216    0.000 3301.403    0.000 layers.py:735(check)
                5760695   24.677    0.000 3117.904    0.001 tensor.py:195(backward)
                5760695   26.375    0.000 3092.429    0.001 __init__.py:68(backward)
                1921986 2442.482    0.001 3041.355    0.002 replaybuffer.py:52(sample_data)
                5760695 2945.836    0.001 2945.836    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3854969  115.527    0.000 2632.166    0.001 agent.py:49(__call__)
                1921986 1084.673    0.001 2371.128    0.001 agent.py:88(interveen)
               25623161 2241.193    0.000 2241.193    0.000 {built-in method tensor}
               30751784 1215.752    0.000 2170.122    0.000 layer.py:167(NoRock_update)
               21223801   13.289    0.000 2126.903    0.000 game.py:37(board)
                1921986 1207.947    0.001 2050.424    0.001 replaybuffer.py:28(teleporter_save_data)
               26948428   64.881    0.000 1967.388    0.000 conv.py:398(forward)
               26948428   40.882    0.000 1870.733    0.000 conv.py:390(_conv_forward)
              191913582  313.944    0.000 1870.416    0.000 layers.py:729(isFree)
               26948428 1829.851    0.000 1829.851    0.000 {built-in method conv2d}
             1365139524 1324.008    0.000 1556.472    0.000 layer.py:95(isFree)
                1921986  974.094    0.001 1480.389    0.001 agent.py:67(modify)
               36578670   75.172    0.000 1471.253    0.000 linear.py:93(forward)
               36578670   30.068    0.000 1354.109    0.000 functional.py:1737(linear)
               36578670 1317.217    0.000 1317.217    0.000 {built-in method torch._C._nn.linear}
               24970500  971.626    0.000  971.626    0.000 {built-in method cat}
                1916723   38.920    0.000  892.486    0.000 agent.py:171(__call__)
                1921986   37.566    0.000  837.716    0.000 agent.py:112(__call__)
               86158952  819.644    0.000  819.644    0.000 {built-in method clone}
                5776955   41.822    0.000  799.117    0.000 agent.py:59(modify_board)
             2858639302  538.735    0.000  769.079    0.000 enum.py:646(__hash__)
               50052884   42.737    0.000  757.332    0.000 activation.py:713(forward)
              192159339  175.843    0.000  735.229    0.000 {built-in method builtins.any}
              191913582  480.828    0.000  731.750    0.000 layers.py:286(check)
              107525956  722.058    0.000  722.058    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              192198700   90.546    0.000  718.291    0.000 {built-in method builtins.all}
               50052884   42.470    0.000  714.595    0.000 functional.py:1364(leaky_relu)
                1921986  541.121    0.000  685.411    0.000 replaybuffer.py:58(CF_save_data)
                1961348   23.474    0.000  664.702    0.000 layers.py:740(restart)
               50052884  664.063    0.000  664.063    0.000 {built-in method torch._C._nn.leaky_relu}
              971032769  249.048    0.000  652.354    0.000 layers.py:690(<genexpr>)
                5760695  118.886    0.000  650.961    0.000 optimizer.py:189(zero_grad)
              107525956  643.233    0.000  643.233    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              191913582  365.689    0.000  608.570    0.000 layers.py:246(check)
              598085989  573.613    0.000  573.613    0.000 layer.py:146(elements)
             1712136168  459.017    0.000  559.387    0.000 layers.py:700(<genexpr>)
                5776955  529.550    0.000  529.550    0.000 {built-in method torch._C._nn.one_hot}
                1961348   11.468    0.000  467.865    0.000 level.py:8(__init__)
                1921986   37.959    0.000  467.501    0.000 replaybuffer.py:18(stacker)
                1916723   35.526    0.000  450.523    0.000 replaybuffer.py:48(stacker)
               53762978  424.135    0.000  424.135    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               53762978  377.333    0.000  377.333    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1961348   43.696    0.000  365.815    0.000 levels.py:164(generate)
              192198700  242.820    0.000  360.607    0.000 layers.py:113(isDone)
             3731552238  352.276    0.000  352.276    0.000 layer.py:91(positions)
               53762978  348.199    0.000  348.199    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               53762978  347.817    0.000  347.817    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                7766668  129.291    0.000  338.810    0.000 random.py:315(sample)
        4248052656/4248052653  288.639    0.000  325.348    0.000 {built-in method builtins.len}
              191913582  197.883    0.000  318.987    0.000 layers.py:273(check)
              191913582  197.738    0.000  314.825    0.000 layers.py:313(check)
              376340930  255.038    0.000  314.697    0.000 tensor.py:906(grad)
                1921986  170.890    0.000  291.619    0.000 collector.py:46(collect)
                3854969   97.292    0.000  280.252    0.000 exploration.py:53(softmaxer)
              191913582  186.385    0.000  277.414    0.000 layers.py:48(check)
                5760695   10.146    0.000  277.279    0.000 loss.py:527(forward)
                5760695   29.303    0.000  267.134    0.000 functional.py:2898(mse_loss)
                3922696   38.980    0.000  264.126    0.000 level.py:41(notUsed)
                1921986   45.838    0.000  257.039    0.000 agent.py:277(counterfact_check)
               53762978  251.406    0.000  251.406    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             2858661509  230.348    0.000  230.348    0.000 {built-in method builtins.hash}
              191913582  140.858    0.000  208.353    0.000 layers.py:23(check)
               93852630  200.236    0.000  200.236    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              268845577  122.190    0.000  169.984    0.000 layer.py:130(add)
               15690784   22.783    0.000  167.792    0.000 layer.py:69(restart)
                5760695  162.283    0.000  162.283    0.000 {built-in method torch._C._nn.mse_loss}
              239122421  108.858    0.000  161.782    0.000 random.py:250(_randbelow_with_getrandbits)
              169067497  105.138    0.000  158.847    0.000 layer.py:126(remove)
             1740373942  148.921    0.000  148.921    0.000 {method 'random' of '_random.Random' objects}
               13453902  148.201    0.000  148.201    0.000 {built-in method sum}
                3843974  147.701    0.000  147.701    0.000 {built-in method nonzero}
                5761272  145.227    0.000  145.227    0.000 {built-in method max}
               26948428   20.964    0.000  129.015    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9512492: <ReTest1_0> in cluster <dcc> Done

Job <ReTest1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 13 13:40:46 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 13 16:13:37 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 16:13:37 2021
Terminated at Wed Apr 14 04:08:57 2021
Results reported at Wed Apr 14 04:08:57 2021

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

    CPU time :                                   42807.96 sec.
    Max Memory :                                 6935 MB
    Average Memory :                             5134.26 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9449.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42921 sec.
    Turnaround time :                            52091 sec.

The output (if any) is above this job summary.

