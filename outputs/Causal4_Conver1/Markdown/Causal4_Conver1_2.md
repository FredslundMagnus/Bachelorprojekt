
# Parameters

    Name :                      Causal4_Conver1-2
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67890814501 function calls (67596222282 primitive calls) in 86114.05 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.046 86114.046 {built-in method builtins.exec}
                      1    4.281    4.281 86114.046 86114.046 <string>:1(<module>)
                      1  329.820  329.820 86109.765 86109.765 main.py:79(CFagent)
                9196662   32.776    0.000 27507.641    0.003 agent.py:29(learn)
                9196653  690.999    0.000 22941.249    0.002 learner.py:42(Qlearn)
                3065554   13.765    0.000 18747.317    0.006 game.py:41(step)
                3065554   19.017    0.000 17988.938    0.006 layers.py:718(step)
        329358243/34767715 1319.726    0.000 12091.763    0.000 module.py:866(_call_impl)
                3065554  261.869    0.000 11467.679    0.004 layers.py:17(step)
               25571062   72.058    0.000 11361.553    0.000 network.py:27(forward)
              306531282  800.477    0.000 11180.379    0.000 layer.py:98(move)
               25571062  346.011    0.000 11135.595    0.000 container.py:117(forward)
                3065554 1352.957    0.000 11074.794    0.004 agent.py:212(counterfact)
                3065554  314.892    0.000 10620.206    0.003 agent.py:54(_learn)
                3065554  312.412    0.000 9828.928    0.003 agent.py:204(_learn)
                9196653   80.655    0.000 9764.945    0.001 optimizer.py:84(wrapper)
                9196653   38.614    0.000 9388.209    0.001 grad_mode.py:24(decorate_context)
                9196653  266.972    0.000 9262.875    0.001 adam.py:55(step)
                9196653 1887.112    0.000 8700.710    0.001 _functional.py:53(adam)
                3065554   90.767    0.000 7004.742    0.002 agent.py:117(_learn)
              306531282 1347.693    0.000 6954.443    0.000 layers.py:735(check)
                3065555  423.162    0.000 6477.904    0.002 layers.py:684(update)
                3065554 3167.437    0.001 5907.296    0.002 replaybuffer.py:28(teleporter_save_data)
                8185770  218.170    0.000 5902.346    0.001 agent.py:49(__call__)
                9196653   38.184    0.000 5689.996    0.001 tensor.py:195(backward)
                9196653   35.000    0.000 5650.400    0.001 __init__.py:68(backward)
               51029474 5472.732    0.000 5472.732    0.000 {built-in method tensor}
                9196653 5410.355    0.001 5410.355    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               43948930   29.744    0.000 5270.385    0.000 game.py:37(board)
                3065554 4269.525    0.001 5264.857    0.002 replaybuffer.py:22(sample_data)
                3065554 2969.964    0.001 5174.841    0.002 agent.py:88(interveen)
                3065554 4025.679    0.001 4989.558    0.002 replaybuffer.py:67(sample_data)
               51142124  108.477    0.000 4025.855    0.000 conv.py:398(forward)
               61311090 2399.640    0.000 3977.908    0.000 layer.py:151(update)
               51142124   79.243    0.000 3867.637    0.000 conv.py:390(_conv_forward)
               51142124 3788.394    0.000 3788.394    0.000 {built-in method conv2d}
               70582078  136.332    0.000 3233.056    0.000 linear.py:93(forward)
               70582078   59.975    0.000 3029.144    0.000 functional.py:1737(linear)
                2057540   44.833    0.000 2988.148    0.001 agent.py:176(choose_action)
               70582078 2955.323    0.000 2955.323    0.000 {built-in method torch._C._nn.linear}
              306531282  550.033    0.000 2873.521    0.000 layers.py:729(isFree)
                3065554 1830.753    0.001 2722.129    0.001 agent.py:67(modify)
              203838273 2630.610    0.000 2630.610    0.000 {built-in method clone}
             2896024497 1909.075    0.000 2323.488    0.000 layer.py:95(isFree)
               96153140   74.913    0.000 1802.688    0.000 activation.py:713(forward)
              171670844 1799.055    0.000 1799.055    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3065554 1323.389    0.000 1780.521    0.001 replaybuffer.py:73(CF_save_data)
               96153140   84.192    0.000 1727.775    0.000 functional.py:1364(leaky_relu)
               41906819 1722.787    0.000 1722.787    0.000 {built-in method cat}
                5104745   56.747    0.000 1712.147    0.000 layers.py:740(restart)
               11251324   75.095    0.000 1626.904    0.000 agent.py:59(modify_board)
               96153140 1626.199    0.000 1626.199    0.000 {built-in method torch._C._nn.leaky_relu}
              171670844 1565.178    0.000 1565.178    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3065545   53.124    0.000 1537.320    0.001 agent.py:172(__call__)
             6161717171 1014.983    0.000 1447.793    0.000 enum.py:646(__hash__)
                3065554   51.308    0.000 1433.147    0.000 agent.py:112(__call__)
                9196653  216.256    0.000 1339.966    0.000 optimizer.py:189(zero_grad)
              304516310  295.076    0.000 1288.081    0.000 {built-in method builtins.any}
                5104745   24.845    0.000 1202.421    0.000 level.py:8(__init__)
              306531282  824.727    0.000 1086.489    0.000 layers.py:77(check)
               11251324 1038.699    0.000 1038.699    0.000 {built-in method torch._C._nn.one_hot}
              306531282  665.103    0.000 1037.989    0.000 layers.py:246(check)
             3315958305  816.289    0.000  993.004    0.000 layers.py:700(<genexpr>)
                5104745  155.879    0.000  980.272    0.000 levels.py:199(generate)
               85835422  980.182    0.000  980.182    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              306531282  569.209    0.000  945.301    0.000 layers.py:286(check)
             1344842731  901.643    0.000  901.643    0.000 layer.py:146(elements)
               85835422  835.619    0.000  835.619    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               85835422  811.835    0.000  811.835    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              306555500  124.992    0.000  807.949    0.000 {built-in method builtins.all}
               85835422  795.632    0.000  795.632    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3065554   59.016    0.000  781.278    0.000 replaybuffer.py:18(stacker)
                3065545   59.984    0.000  757.555    0.000 replaybuffer.py:63(stacker)
             1503043819  356.749    0.000  717.782    0.000 layers.py:690(<genexpr>)
               10209490   76.470    0.000  672.127    0.000 level.py:41(notUsed)
             7746319930  662.043    0.000  662.043    0.000 layer.py:91(positions)
              218155142  651.299    0.000  651.299    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3065554  380.785    0.000  629.545    0.000 collector.py:46(collect)
               85835422  620.453    0.000  620.453    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8185770  220.959    0.000  609.512    0.000 exploration.py:53(softmaxer)
              306531282  452.507    0.000  601.653    0.000 layers.py:62(check)
        8055624287/8055624284  525.792    0.000  586.036    0.000 {built-in method builtins.len}
              600848038  390.277    0.000  485.555    0.000 tensor.py:906(grad)
               16340598  183.929    0.000  482.002    0.000 random.py:315(sample)
              306531282  303.199    0.000  469.126    0.000 layers.py:273(check)
              306531282  300.693    0.000  467.951    0.000 layers.py:313(check)
                9196653   12.959    0.000  442.736    0.000 loss.py:527(forward)
                2057540  438.306    0.000  438.306    0.000 agent.py:187(convert_values)
               51047450   61.803    0.000  437.621    0.000 layer.py:69(restart)
             6161752146  432.816    0.000  432.816    0.000 {built-in method builtins.hash}
                9196653   33.675    0.000  429.777    0.000 functional.py:2898(mse_loss)
              306531282  271.948    0.000  405.323    0.000 layers.py:48(check)
              323540690  267.006    0.000  355.495    0.000 layer.py:126(remove)
              306531282  217.206    0.000  316.717    0.000 layers.py:23(check)
              613361614  229.093    0.000  315.548    0.000 layer.py:130(add)
               51142124   38.879    0.000  300.786    0.000 flatten.py:39(forward)
                9196653  284.327    0.000  284.327    0.000 {built-in method torch._C._nn.mse_loss}
              207507434  266.119    0.000  266.119    0.000 level.py:32(inverse)
               18393324  265.515    0.000  265.515    0.000 {built-in method sum}
                6131110  262.128    0.000  262.128    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579162: <Causal4_Conver1_2> in cluster <dcc> Done

Job <Causal4_Conver1_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:06 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 28 08:28:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 08:28:28 2021
Terminated at Thu Apr 29 08:23:49 2021
Results reported at Thu Apr 29 08:23:49 2021

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

    CPU time :                                   85901.12 sec.
    Max Memory :                                 9028 MB
    Average Memory :                             6207.52 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7356.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86123 sec.
    Turnaround time :                            193183 sec.

The output (if any) is above this job summary.

