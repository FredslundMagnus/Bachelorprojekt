
# Parameters

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH_2-1
    Main :                      Load_Cfagent
    Level :                     Levels.Coconuts
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       1
    Load name :                 Coconuts_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      68681294961 function calls (68296638916 primitive calls) in 86110.43 seconds

##    Ordered by: cumulative time
   List reduced from 433 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.434 86110.434 {built-in method builtins.exec}
                      1    4.252    4.252 86110.434 86110.434 <string>:1(<module>)
                      1  334.290  334.290 86106.182 86106.182 main.py:109(Load_Cfagent)
                9730230   33.119    0.000 23776.097    0.002 agent.py:29(learn)
                3243410 1677.898    0.001 19694.719    0.006 agent.py:212(counterfact)
                9730230  586.346    0.000 19421.831    0.002 learner.py:42(Qlearn)
                3243410   13.120    0.000 18818.357    0.006 game.py:42(step)
                3243410   17.652    0.000 18174.440    0.006 layers.py:827(step)
        427519026/42865802 1733.951    0.000 13725.697    0.000 module.py:866(_call_impl)
               33135572   95.863    0.000 12956.828    0.000 network.py:28(forward)
               33135572  411.872    0.000 12639.919    0.000 container.py:117(forward)
                3243410  294.543    0.000 11853.452    0.004 layers.py:17(step)
              323500219 1153.676    0.000 11530.368    0.000 layer.py:106(move)
                3243410  325.440    0.000 9228.410    0.003 agent.py:54(_learn)
                3243410  322.404    0.000 8484.195    0.003 agent.py:204(_learn)
                9730230   77.596    0.000 7607.011    0.001 optimizer.py:84(wrapper)
               94941975 7572.692    0.000 7572.692    0.000 {built-in method tensor}
               87787450   50.396    0.000 7433.097    0.000 game.py:38(board)
               11695428  292.755    0.000 7348.509    0.001 agent.py:49(__call__)
                9730230   42.375    0.000 7253.978    0.001 grad_mode.py:24(decorate_context)
              323500219 1246.193    0.000 7190.183    0.000 layers.py:844(check)
                9730230  302.260    0.000 7124.379    0.001 adam.py:55(step)
                5223094   98.666    0.000 6975.334    0.001 agent.py:176(choose_action)
                9730230 1495.806    0.000 6499.240    0.001 _functional.py:53(adam)
                3243410  472.921    0.000 6279.059    0.002 layers.py:793(update)
                3243410   99.203    0.000 6008.822    0.002 agent.py:117(_learn)
               90815466 2977.976    0.000 5235.756    0.000 layer.py:159(update)
                9730230   33.031    0.000 5089.609    0.001 tensor.py:195(backward)
                9730230   37.840    0.000 5055.275    0.001 __init__.py:68(backward)
                3243410 4051.101    0.001 5019.516    0.002 replaybuffer.py:22(sample_data)
                3243410 3984.558    0.001 4922.457    0.002 replaybuffer.py:67(sample_data)
                9730230 4829.201    0.000 4829.201    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               66271144  149.222    0.000 4645.797    0.000 conv.py:398(forward)
               66271144   96.856    0.000 4422.984    0.000 conv.py:390(_conv_forward)
               66271144 4326.128    0.000 4326.128    0.000 {built-in method conv2d}
                3243410 1975.137    0.001 4013.270    0.001 agent.py:88(interveen)
                3243410 2227.569    0.001 3961.832    0.001 replaybuffer.py:28(teleporter_save_data)
               92919896  197.148    0.000 3567.660    0.000 linear.py:93(forward)
               92919896   77.486    0.000 3266.531    0.000 functional.py:1737(linear)
               92919896 3170.151    0.000 3170.151    0.000 {built-in method torch._C._nn.linear}
              323500219  492.924    0.000 2396.670    0.000 layers.py:838(isFree)
                3243410 1518.284    0.000 2307.495    0.001 agent.py:67(modify)
              323500219 1535.907    0.000 2161.122    0.000 layers.py:471(check)
                2655280   32.411    0.000 2046.105    0.001 layers.py:849(restart)
             2140387311 1595.565    0.000 1903.746    0.000 layer.py:103(isFree)
              126055468  108.445    0.000 1903.716    0.000 activation.py:713(forward)
               14938838   90.755    0.000 1864.788    0.000 agent.py:59(modify_board)
              323500219 1326.965    0.000 1836.915    0.000 layers.py:77(check)
              126055468  106.978    0.000 1795.271    0.000 functional.py:1364(leaky_relu)
                2655280   14.633    0.000 1751.307    0.001 level.py:8(__init__)
               47372938 1696.713    0.000 1696.713    0.000 {built-in method cat}
              126055468 1665.849    0.000 1665.849    0.000 {built-in method torch._C._nn.leaky_relu}
              168051745 1629.732    0.000 1629.732    0.000 {built-in method clone}
                2655280  109.868    0.000 1597.342    0.001 levels.py:277(generate)
             5960364414 1075.503    0.000 1550.047    0.000 enum.py:646(__hash__)
                3243410   52.696    0.000 1438.238    0.000 agent.py:172(__call__)
                5223094 1218.799    0.000 1409.183    0.000 agent.py:187(convert_values)
               23679970  237.984    0.000 1393.863    0.000 level.py:41(notUsed)
                3243410   47.998    0.000 1332.503    0.000 agent.py:112(__call__)
              181630960 1279.433    0.000 1279.433    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               14938838 1213.371    0.000 1213.371    0.000 {built-in method torch._C._nn.one_hot}
             1251239537 1194.926    0.000 1194.926    0.000 layer.py:154(elements)
              181630960 1135.035    0.000 1135.035    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              331415949  264.145    0.000 1125.512    0.000 {built-in method builtins.any}
                9730230  200.810    0.000 1115.692    0.000 optimizer.py:189(zero_grad)
                3243410  792.038    0.000  993.202    0.000 replaybuffer.py:73(CF_save_data)
              323500219  656.994    0.000  866.950    0.000 layers.py:62(check)
             2573485760  700.113    0.000  861.367    0.000 layers.py:809(<genexpr>)
            11544244972  745.388    0.000  828.373    0.000 {built-in method builtins.len}
              324341000   81.532    0.000  803.864    0.000 {built-in method builtins.all}
              695867274  165.021    0.000  763.503    0.000 layers.py:799(<genexpr>)
               90815480  735.127    0.000  735.127    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3243410   56.578    0.000  732.305    0.000 replaybuffer.py:18(stacker)
               11695428  275.066    0.000  722.991    0.000 exploration.py:53(softmaxer)
                3243410   55.779    0.000  709.682    0.000 replaybuffer.py:63(stacker)
             7560447625  673.233    0.000  673.233    0.000 layer.py:99(positions)
               23679970   20.278    0.000  662.276    0.000 level.py:38(elementsIn)
               90815480  640.233    0.000  640.233    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               90815480  601.257    0.000  601.257    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               90815480  589.764    0.000  589.764    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              324341000  394.593    0.000  586.460    0.000 layers.py:113(isDone)
              635708360  407.409    0.000  505.991    0.000 tensor.py:906(grad)
                3243410  288.531    0.000  489.696    0.000 collector.py:46(collect)
             5960401517  474.551    0.000  474.551    0.000 {built-in method builtins.hash}
              323500219  316.705    0.000  470.335    0.000 layers.py:48(check)
                6486820  172.777    0.000  452.474    0.000 random.py:315(sample)
               90815480  450.646    0.000  450.646    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              386049973  319.831    0.000  447.735    0.000 layer.py:134(remove)
               23679970  209.936    0.000  428.219    0.000 level.py:39(<listcomp>)
                9730230   13.721    0.000  412.203    0.000 loss.py:527(forward)
                9730230   37.940    0.000  398.482    0.000 functional.py:2898(mse_loss)
              186233993  376.830    0.000  376.830    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              323500219  250.105    0.000  360.634    0.000 layers.py:23(check)
               90815466  318.737    0.000  318.737    0.000 layer.py:171(<listcomp>)
               66271144   53.889    0.000  311.640    0.000 flatten.py:39(forward)
             1091433311  291.802    0.000  291.802    0.000 level.py:32(inverse)
              535866874  209.583    0.000  287.305    0.000 layer.py:138(add)
               90815466  275.304    0.000  275.304    0.000 layer.py:172(<listcomp>)
               66271144  257.751    0.000  257.751    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               18586960   35.653    0.000  256.133    0.000 layer.py:77(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632956: <Coconuts_Conver4_3counterfactsNOCRASH_2_1> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:02 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 16:43:31 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 16:43:31 2021
Terminated at Thu May 13 16:38:47 2021
Results reported at Thu May 13 16:38:47 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85870.37 sec.
    Max Memory :                                 9414 MB
    Average Memory :                             6264.50 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6970.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86116 sec.
    Turnaround time :                            89865 sec.

The output (if any) is above this job summary.

