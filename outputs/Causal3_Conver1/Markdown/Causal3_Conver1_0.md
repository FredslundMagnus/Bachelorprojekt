
# Parameters

    Name :                      Causal3_Conver1-0
    Main :                      CFagent
    Level :                     Levels.Causal3
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      61407919000 function calls (61105354037 primitive calls) in 86123.16 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86123.157 86123.157 {built-in method builtins.exec}
                      1    4.846    4.846 86123.157 86123.157 <string>:1(<module>)
                      1  394.484  394.484 86118.311 86118.311 main.py:79(CFagent)
                9216585   41.601    0.000 23479.638    0.003 agent.py:29(learn)
                9216585  599.030    0.000 18998.564    0.002 learner.py:42(Qlearn)
                3072195   15.847    0.000 17810.216    0.006 game.py:41(step)
                3072195   21.039    0.000 17119.333    0.006 layers.py:718(step)
        338017528/35454256 1422.901    0.000 11373.357    0.000 module.py:866(_call_impl)
                3072195 1531.366    0.000 10622.207    0.003 agent.py:212(counterfact)
               26237671   74.891    0.000 10621.995    0.000 network.py:27(forward)
               26237671  358.365    0.000 10369.100    0.000 container.py:117(forward)
                3072195  308.469    0.000 9667.615    0.003 layers.py:17(step)
              307219500  510.144    0.000 9331.353    0.000 layer.py:98(move)
                3072195  366.039    0.000 9144.099    0.003 agent.py:54(_learn)
                3072195  360.129    0.000 8321.528    0.003 agent.py:204(_learn)
                3072195 6714.417    0.002 7747.611    0.003 replaybuffer.py:22(sample_data)
                3072195 6579.700    0.002 7566.694    0.002 replaybuffer.py:67(sample_data)
                3072196  467.055    0.000 7396.889    0.002 layers.py:684(update)
                9216585   92.347    0.000 7342.056    0.001 optimizer.py:84(wrapper)
                9216585   47.773    0.000 6966.851    0.001 grad_mode.py:24(decorate_context)
                9216585  309.025    0.000 6821.016    0.001 adam.py:55(step)
                3072195 3791.810    0.001 6471.808    0.002 replaybuffer.py:28(teleporter_save_data)
                9216585 1412.368    0.000 6193.430    0.001 _functional.py:53(adam)
                3072195   99.877    0.000 5951.022    0.002 agent.py:117(_learn)
                8509691  255.001    0.000 5710.327    0.001 agent.py:49(__call__)
              307219500 1112.066    0.000 5356.594    0.000 layers.py:735(check)
                3072195 3188.239    0.001 5209.020    0.002 agent.py:88(interveen)
                9216585   41.415    0.000 4994.217    0.001 tensor.py:195(backward)
                9216585   45.103    0.000 4951.546    0.001 __init__.py:68(backward)
                9216585 4714.754    0.001 4714.754    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               47597800 4363.051    0.000 4363.051    0.000 {built-in method tensor}
               40500403   28.570    0.000 4185.798    0.000 game.py:37(board)
               49155128 2261.315    0.000 3866.698    0.000 layer.py:167(NoRock_update)
               52475342  120.223    0.000 3836.590    0.000 conv.py:398(forward)
               52475342   79.955    0.000 3656.465    0.000 conv.py:390(_conv_forward)
               52475342 3576.509    0.000 3576.509    0.000 {built-in method conv2d}
                2367005   51.204    0.000 3172.742    0.001 agent.py:176(choose_action)
              307219500  489.922    0.000 2958.577    0.000 layers.py:729(isFree)
               72568623  147.021    0.000 2928.646    0.000 linear.py:93(forward)
               72568623   59.766    0.000 2702.419    0.000 functional.py:1737(linear)
              266133810 2666.844    0.000 2666.844    0.000 {built-in method clone}
               72568623 2628.483    0.000 2628.483    0.000 {built-in method torch._C._nn.linear}
             2271563692 2093.639    0.000 2468.655    0.000 layer.py:95(isFree)
                3072195 1661.741    0.001 2460.632    0.001 agent.py:67(modify)
                7411453   78.251    0.000 2375.072    0.000 layers.py:740(restart)
                3072195 1536.960    0.001 2038.353    0.001 replaybuffer.py:73(CF_save_data)
               42303836 1670.321    0.000 1670.321    0.000 {built-in method cat}
                7411453   39.138    0.000 1663.024    0.000 level.py:8(__init__)
               11581886   80.050    0.000 1572.955    0.000 agent.py:59(modify_board)
               98806294   79.399    0.000 1528.609    0.000 activation.py:713(forward)
               98806294   80.533    0.000 1449.210    0.000 functional.py:1364(leaky_relu)
                3072195   63.393    0.000 1439.151    0.000 agent.py:172(__call__)
               98806294 1352.117    0.000 1352.117    0.000 {built-in method torch._C._nn.leaky_relu}
             5109401667  930.023    0.000 1346.857    0.000 enum.py:646(__hash__)
                3072195   58.497    0.000 1343.583    0.000 agent.py:112(__call__)
                7411453  153.164    0.000 1323.389    0.000 levels.py:164(generate)
              307219600  177.231    0.000 1257.824    0.000 {built-in method builtins.all}
              307219500  785.857    0.000 1220.992    0.000 layers.py:286(check)
              302880343  277.642    0.000 1217.024    0.000 {built-in method builtins.any}
              172042920 1211.345    0.000 1211.345    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1954680520  528.684    0.000 1118.962    0.000 layers.py:690(<genexpr>)
              172042920 1075.745    0.000 1075.745    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9216585  197.203    0.000 1072.233    0.000 optimizer.py:189(zero_grad)
               11581886 1040.486    0.000 1040.486    0.000 {built-in method torch._C._nn.one_hot}
              307219500  603.346    0.000 1007.151    0.000 layers.py:246(check)
             1444688107  986.051    0.000  986.051    0.000 layer.py:146(elements)
               14822906  135.252    0.000  962.956    0.000 level.py:41(notUsed)
             2698273323  783.302    0.000  939.381    0.000 layers.py:700(<genexpr>)
                3072195   66.125    0.000  783.055    0.000 replaybuffer.py:18(stacker)
                3072195   68.239    0.000  747.980    0.000 replaybuffer.py:63(stacker)
               86021460  711.876    0.000  711.876    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               20967296  242.692    0.000  623.789    0.000 random.py:315(sample)
               86021460  620.236    0.000  620.236    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               59291624   77.842    0.000  612.589    0.000 layer.py:69(restart)
                8509691  212.324    0.000  588.394    0.000 exploration.py:53(softmaxer)
               86021460  569.809    0.000  569.809    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               86021460  567.527    0.000  567.527    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              280787891  556.528    0.000  556.528    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             6021373371  548.951    0.000  548.951    0.000 layer.py:91(positions)
        6974892402/6974892399  480.649    0.000  539.606    0.000 {built-in method builtins.len}
              307219500  314.594    0.000  502.949    0.000 layers.py:273(check)
              602150304  395.570    0.000  490.224    0.000 tensor.py:906(grad)
              307219500  306.425    0.000  486.764    0.000 layers.py:313(check)
                2367005  483.531    0.000  483.531    0.000 agent.py:187(convert_values)
                3072195  279.479    0.000  475.812    0.000 collector.py:46(collect)
                9216585   16.656    0.000  438.436    0.000 loss.py:527(forward)
              307219500  295.892    0.000  437.285    0.000 layers.py:48(check)
               86021460  427.555    0.000  427.555    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              306267709  328.652    0.000  422.732    0.000 layer.py:126(remove)
                9216585   45.103    0.000  421.781    0.000 functional.py:2898(mse_loss)
             5109436754  416.841    0.000  416.841    0.000 {built-in method builtins.hash}
              676727198  281.102    0.000  389.264    0.000 layer.py:130(add)
               14822906   14.942    0.000  384.948    0.000 level.py:38(elementsIn)
              202893392  262.341    0.000  381.310    0.000 layers.py:113(isDone)
                7411553  193.835    0.000  381.216    0.000 layers.py:36(reset)
              486221569  334.606    0.000  334.606    0.000 level.py:32(inverse)
              307219500  224.135    0.000  333.676    0.000 layers.py:23(check)
              441394460  205.057    0.000  303.256    0.000 random.py:250(_randbelow_with_getrandbits)
                7411453  147.279    0.000  277.515    0.000 level.py:16(<dictcomp>)
               52475342   49.175    0.000  261.759    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579154: <Causal3_Conver1_0> in cluster <dcc> Done

Job <Causal3_Conver1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:05 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 27 04:31:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 04:31:52 2021
Terminated at Wed Apr 28 04:27:36 2021
Results reported at Wed Apr 28 04:27:36 2021

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

    CPU time :                                   85907.61 sec.
    Max Memory :                                 8782 MB
    Average Memory :                             5954.46 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7602.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86145 sec.
    Turnaround time :                            92611 sec.

The output (if any) is above this job summary.

